<script lang="ts">
  import { Popover } from 'bits-ui';
  import CircleCheckIcon from 'lucide-svelte/icons/circle-check';
  import CircleGaugeIcon from 'lucide-svelte/icons/circle-gauge';
  import CircleXIcon from 'lucide-svelte/icons/circle-x';
  import LightbulbIcon from 'lucide-svelte/icons/lightbulb';
  import PieChartIcon from 'lucide-svelte/icons/pie-chart';
  import RefreshCwIcon from 'lucide-svelte/icons/refresh-cw';
  import VideoOffIcon from 'lucide-svelte/icons/video-off';

  import { prettifyDate } from '$lib/utils/date/format';
  import { flyAndScale } from '$lib/utils/transitions/fly-and-scale';

  const date = new Date();

  let isMotorToggled = $state(false);
  let isLedToggled = $state(false);

  let isOnline = $state(true);

  const getStatusClasses = (isOnline: boolean) =>
    isOnline ? 'border-emerald-800 bg-emerald-700' : 'border-red-800 bg-red-700';

  const onToggleMotor = () => {
    isMotorToggled = !isMotorToggled;
  };

  const onToggleLed = () => {
    isLedToggled = !isLedToggled;
  };
</script>

<header class="bg-sky-300 p-3 flex justify-between">
  <h1 class="font-semibold text-xl">Watering Can</h1>
  <Popover.Root>
    <Popover.Trigger
      class="rounded border text-white px-2 flex items-center gap-2 {getStatusClasses(isOnline)}"
      ><CircleCheckIcon size={16} aria-hidden="true" /><span class="sr-only"
        >Status:
      </span>{isOnline ? 'Online' : 'Offline'}</Popover.Trigger
    >
    <Popover.Content
      class="z-30 w-full max-w-[328px] rounded-xl border border-slate-300 bg-slate-100 p-4 shadow-md"
      transition={flyAndScale}
      sideOffset={8}
    >
      <ul>
        <li></li>
        <li></li>
      </ul>
      <p>Motor: Online</p>
      <p>Servo: Online</p>
      <p class="text-sm"><em>Last updated at {prettifyDate(date)}</em></p>
    </Popover.Content>
  </Popover.Root>
</header>

<main class="grid md:grid-cols-3 auto-cols-auto gap-6 m-6">
  <!-- Sensor data -->
  <section
    class="rounded bg-slate-200 p-3 flex flex-col gap-3 border border-slate-400 md:col-span-2"
  >
    <header class="flex justify-between">
      <div>
        <h2 class="text-2xl">Sensor data</h2>
        <p class="italic text-sm">
          Last updated at <time datetime={date.toISOString()}>{prettifyDate(date)}</time>
        </p>
      </div>
      <button
        aria-label="Refresh sensor data"
        class="bg-sky-200 hover:bg-sky-300 active:bg-sky-400 rounded-full shadow border-2 border-sky-400 focus:ring focus-visible:outline-none focus:ring-sky-500 transition-all p-3"
      >
        <RefreshCwIcon />
      </button>
    </header>
    <div class="grid gap-3 md:grid-flow-col auto-cols-auto">
      <figure class="bg-white p-2 flex flex-col gap-2 rounded">
        <div class="flex place-content-center p-10 border border-black rounded">
          <PieChartIcon size={48} />
        </div>
        <figcaption class="text-lg">Temperature</figcaption>
      </figure>
      <figure class="bg-white p-2 flex flex-col gap-2 rounded">
        <div class="flex place-content-center p-10 border border-black rounded">
          <PieChartIcon size={48} />
        </div>
        <figcaption class="text-lg">Moisture</figcaption>
      </figure>
    </div>
  </section>
  <!-- Actions -->
  <section class="rounded bg-purple-200 p-3 flex flex-col gap-3 border border-purple-400">
    <header>
      <h2 class="text-2xl">Actions</h2>
    </header>
    <div class="grid gap-3">
      <button
        class="bg-orange-200 hover:bg-orange-300 active:bg-orange-400 rounded shadow border-2 border-orange-400 focus:ring focus-visible:outline-none focus:ring-orange-500 transition-all p-3 flex flex-col gap-2 place-content-center items-center aria-checked:bg-orange-400"
        role="switch"
        aria-checked={isLedToggled}
        onclick={onToggleLed}><LightbulbIcon />Toggle LEDs</button
      >
      <button
        class="bg-emerald-200 hover:bg-emerald-300 active:bg-emerald-400 rounded shadow border-2 border-emerald-400 focus:ring focus-visible:outline-none focus:ring-emerald-500 transition-all p-3 flex flex-col gap-2 place-content-center items-center aria-checked:bg-emerald-400"
        role="switch"
        aria-checked={isMotorToggled}
        onclick={onToggleMotor}><CircleGaugeIcon />Toggle motor</button
      >
    </div>
  </section>
  <!-- Camera feed -->
  <section
    class="rounded bg-lime-200 p-3 flex flex-col gap-3 border border-lime-400 md:col-span-full"
  >
    <figure class="flex flex-col gap-2 rounded">
      <figcaption class="text-2xl">Camera Feed</figcaption>
      <div class="flex place-content-center p-10 border border-black rounded">
        <VideoOffIcon size={48} />
      </div>
    </figure>
  </section>
</main>
