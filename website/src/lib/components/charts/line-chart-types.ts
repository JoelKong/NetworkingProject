import type { AxisScale, AxisDomain } from 'd3';
import type { Snippet } from 'svelte';

export interface LineChartProps {
  data: number[];
  formatPoint: (data: number) => string;

  tooltip?: Snippet<[number, { left: number; top: number }]>;
  // Unused for now
  axes?: {
    x: AxisScale<AxisDomain>;
    y: AxisScale<AxisDomain>;
  };
}
