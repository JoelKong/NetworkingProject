<script lang="ts">
  import LineChart from '$lib/components/charts/LineChart.svelte';
  import { prettifyDate } from '$lib/utils/date/format';
  import type { SensorDashboardCardProps } from './sensor-dashboard-card-types';

  let {
    klass,
    lastUpdated,
    humidityData,
    temperatureData,
    formatDate = prettifyDate
  }: SensorDashboardCardProps = $props();
</script>

<section class="rounded bg-slate-200 p-3 flex flex-col gap-3 border border-slate-400 {klass}">
  <header class="flex justify-between">
    <div>
      <h2 class="text-2xl">Sensor data</h2>
      <p class="italic text-sm">
        Last updated at <time datetime={lastUpdated.toISOString()}>{formatDate(lastUpdated)}</time>
      </p>
    </div>
  </header>
  <div class="grid gap-3 md:grid-flow-col auto-cols-auto">
    <figure class="bg-white p-2 flex flex-col gap-2 rounded">
      <LineChart data={temperatureData} formatPoint={(d) => `${d}°C`} />
      <figcaption class="text-lg">Temperature</figcaption>
    </figure>
    <figure class="bg-white p-2 flex flex-col gap-2 rounded">
      <LineChart data={humidityData} formatPoint={(d) => `${d}%`} />
      <figcaption class="text-lg">Humidity</figcaption>
    </figure>
  </div>
</section>
