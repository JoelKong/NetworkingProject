<script lang="ts">
  import CircleGaugeIcon from 'lucide-svelte/icons/circle-gauge';

  import type { ActionsDashboardCardProps } from './actions-dashboard-card-types';

  let { onActivateSensorsClick }: ActionsDashboardCardProps = $props();
</script>

<section class="rounded bg-purple-200 p-3 flex flex-col gap-3 border border-purple-400">
  <header>
    <h2 class="text-2xl">Actions</h2>
  </header>
  <div class="grid gap-3">
    <button
      class="bg-blue-200 hover:bg-blue-300 active:bg-blue-400 rounded shadow border-2 border-blue-400 focus:ring focus-visible:outline-none focus:ring-blue-500 transition-all p-3 flex flex-col gap-2 place-content-center items-center"
      onclick={onActivateSensorsClick}><CircleGaugeIcon />Activate sensors</button
    >
  </div>
</section>
