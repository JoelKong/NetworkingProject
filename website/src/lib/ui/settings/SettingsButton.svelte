<script lang="ts">
  import { Dialog } from 'bits-ui';
  import SettingsIcon from 'lucide-svelte/icons/settings';

  import { fade } from 'svelte/transition';

  import { settings, type Settings } from '$lib/data/settings';

  import SettingsDialogContent from './SettingsDialogContent.svelte';

  const onSettingsChange = (s: Settings) => {
    $settings = s;
  };
</script>

<Dialog.Root>
  <Dialog.Trigger
    class="border-2 border-slate-300 bg-white hover:bg-slate-100 active:bg-slate-200 p-2 rounded-full focus-visible:outline-none focus:ring ring-slate-400 transition-all"
  >
    <SettingsIcon />
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay
      transition={fade}
      transitionConfig={{ duration: 150 }}
      class="fixed inset-0 z-50 bg-black/70"
    />
    <SettingsDialogContent
      settings={$settings}
      klass="fixed left-[50%] top-[50%] z-50 w-full max-w-[94%] translate-x-[-50%] translate-y-[-50%] rounded-md border bg-white p-5 shadow-popover outline-none sm:max-w-[490px] md:w-full"
      {onSettingsChange}
    />
  </Dialog.Portal>
</Dialog.Root>
