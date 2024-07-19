import type { Settings } from '$lib/data/settings';

export interface SettingsDialogContentProps {
  klass: string;
  settings: Settings;

  onSettingsChange: (settings: Settings) => void;
}
