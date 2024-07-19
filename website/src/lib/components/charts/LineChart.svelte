<script lang="ts">
  import { extent, line as d3Line, scaleLinear, select, axisLeft, axisBottom } from 'd3';
  import type { LineChartProps } from './line-chart-types';
  import { flyAndScale } from '$lib/utils/transitions/fly-and-scale';
  import type { TransitionConfig } from 'svelte/transition';

  let { data, formatPoint, tooltip }: LineChartProps = $props();

  let width = 640;
  let height = 400;
  let marginTop = 20;
  let marginRight = 20;
  let marginBottom = 30;
  let marginLeft = 40;

  let gx: SVGGElement;
  let gy: SVGGElement;
  let path: SVGPathElement;

  let x = $derived(scaleLinear([0, data.length - 1], [marginLeft, width - marginRight]));
  let y = $derived(
    scaleLinear(extent(data) as [number, number], [height - marginBottom, marginTop])
  );
  let line = $derived(d3Line((d, i) => x(i), y));
  $effect(() => {
    select(gy).call(axisLeft(y));
    select(gx).call(axisBottom(x));
    x.domain([0, data.length - 1]);
    y.domain(extent(data) as [number, number]);
  });

  let pathLen = $state(0);

  let pathDashArray = $derived(`${pathLen} ${pathLen}`);

  $effect(() => {
    // Arrays don't get mutated, so Svelte isn't aware that the data has changed.
    // Hence, we need to access the .length property which does get updated when the
    // array is modified
    // eslint-disable-next-line @typescript-eslint/no-unused-expressions
    data.length;
    pathLen = path.getTotalLength();
  });

  let hoveredItem = $state<number | null>(null);

  let tooltipPos = $state({ left: 0, top: 0 });

  let isCircleFocused = $state(false);

  const onCircleHover = (d: number) => (e: MouseEvent) => {
    console.log(e.type);
    hoveredItem = d;
    tooltipPos = { left: e?.pageX ?? 0, top: e?.pageY ?? 0 };
  };

  const onCircleUnHover = () => {
    hoveredItem = null;
    isCircleFocused = false;
  };

  const onCircleFocus = (d: number) => () => {
    isCircleFocused = true;
    hoveredItem = d;
    const rect = document.activeElement!.getBoundingClientRect();
    tooltipPos = { left: rect.left, top: rect.top };
  };

  const maybe = (
    node: Element,
    opts: { fn: (node: Element, opts: any) => TransitionConfig; [key: string]: any }
  ) => {
    if (!isCircleFocused) return opts.fn(node, opts);
  };
</script>

<svg viewBox={`0 0 ${width} ${height}`}>
  <g bind:this={gx} transform="translate(0,{height - marginBottom})" />
  <g bind:this={gy} transform="translate({marginLeft},0)" />
  <path
    fill="none"
    bind:this={path}
    stroke="currentColor"
    stroke-width="1.5"
    d={line(data)}
    class="transition-all duration-500"
    style:stroke-dasharray={pathDashArray}
  />
  <g fill="white" stroke="currentColor" stroke-width="1.5">
    {#each data as d, i}
      <circle
        key={i}
        cx={x(i)}
        cy={y(d)}
        r="2.5"
        fill="white"
        role="presentation"
        tabindex="0"
        onmouseover={onCircleHover(d)}
        onfocus={onCircleFocus(d)}
        onmouseout={onCircleUnHover}
        onblur={onCircleUnHover}
      />
    {/each}
  </g>
</svg>

<!-- Tooltip -->

{#if hoveredItem}
  {#if tooltip}
    {@render tooltip(hoveredItem, tooltipPos)}
  {:else}
    <div
      class="absolute border border-black bg-slate-200 p-2"
      style:left={`${tooltipPos.left - 7.5}px`}
      style:top={`${tooltipPos.top - 50}px`}
      transition:maybe|global={{ fn: flyAndScale, duration: isCircleFocused ? 0 : 200 }}
    >
      {formatPoint?.(hoveredItem) ?? hoveredItem}
    </div>
  {/if}
{/if}
