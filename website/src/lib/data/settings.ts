import { persisted } from 'svelte-persisted-store';

export interface Settings {
  intervalMs: number;
  maxSensorPoints: number;
}

export const defaultSettings: Settings = {
  intervalMs: 3000,
  maxSensorPoints: 30
};

export const settingsKey = 'water:settings';
export const settings = persisted<Settings>(settingsKey, defaultSettings);

export const hasNoSettings = (settings: Settings) => Object.keys(settings).length === 0;

export const settingsOrDefault = (settings: Settings) =>
  hasNoSettings(settings) ? defaultSettings : settings;
