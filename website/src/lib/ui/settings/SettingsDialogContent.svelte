<script lang="ts">
  import { Dialog } from 'bits-ui';

  import { flyAndScale } from '$lib/utils/transitions/fly-and-scale';

  import type { SettingsDialogContentProps } from './settings-dialog-types';
  import { defaultSettings, settingsOrDefault } from '$lib/data/settings';

  let { klass, settings, onSettingsChange }: SettingsDialogContentProps = $props();

  let tempSettings = $state(settingsOrDefault(settings));

  const onSaveClick = () => {
    onSettingsChange(tempSettings);
  };

  const onResetClick = () => {
    tempSettings = defaultSettings;
  };
</script>

<Dialog.Content class={klass} transition={flyAndScale}>
  <form class="flex flex-col gap-3">
    <Dialog.Title class="text-xl font-semibold">Settings</Dialog.Title>

    <label class="flex flex-col gap">
      <span
        >Sync interval (in milli-seconds) <em class="text-sm">(default: <code>3000</code>)</em
        >:</span
      >
      <input
        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 transition-all"
        type="number"
        min="3"
        bind:value={tempSettings.intervalMs}
        required
      />
    </label>

    <label class="flex flex-col gap">
      <span>Max number of data points <em class="text-sm">(default: 30)</em>:</span>
      <input
        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 transition-all"
        type="number"
        min="1"
        max="240"
        bind:value={tempSettings.maxSensorPoints}
        required
      />
    </label>

    <footer class="flex gap-3">
      <button
        onclick={onResetClick}
        class="px-3 py-2 bg-red-500 text-white hover:bg-red-600 active:bg-red-700 transition-all rounded-md focus-visible:outline-none focus:ring ring-red-600 mr-auto"
        >Reset</button
      >
      <Dialog.Close
        type="button"
        class="px-3 py-2 hover:bg-slate-100 active:bg-slate-200 transition-all rounded-md focus-visible:outline-none focus:ring ring-slate-300"
        >Cancel</Dialog.Close
      >
      <Dialog.Close
        type="submit"
        class="px-3 py-2 bg-indigo-500 text-white hover:bg-indigo-600 active:bg-indigo-700 transition-all rounded-md focus-visible:outline-none focus:ring ring-indigo-800"
        onclick={onSaveClick}>Save</Dialog.Close
      >
    </footer>
  </form>
</Dialog.Content>
