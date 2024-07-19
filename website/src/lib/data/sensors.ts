import { writable } from 'svelte/store';

export const temperatureSensor = writable<number[]>([]);
export const humiditySensor = writable<number[]>([]);

export const addTemperature = (tempCelsius: number) => {
  temperatureSensor.update((arr) => [...arr, tempCelsius]);
};

export const addHumidity = (humidity: number) => {
  humiditySensor.update((arr) => [...arr, humidity]);
};
