<script lang="ts">
  import { type Status, statuses } from '$lib/data/status';

  let { status: statusEnum }: { status: Status } = $props();

  let currStatus = $derived(statuses[statusEnum]);
</script>

<svelte:component
  this={currStatus.icon}
  size={16}
  aria-hidden="true"
  class={currStatus.iconClass}
/><span class="sr-only">Status: </span>{currStatus.text}
