import CircleCheckIcon from 'lucide-svelte/icons/circle-check';
import CircleXIcon from 'lucide-svelte/icons/circle-x';
import LoaderCircleIcon from 'lucide-svelte/icons/loader-circle';
import type { Component, ComponentType } from 'svelte';

export enum Status {
  Loading = 'loading',
  Online = 'online',
  Offline = 'offline'
}

interface StatusData {
  classes: string;
  icon: ComponentType;
  iconClass?: string;
  text: string;
}

export const statuses: Record<Status, StatusData> = {
  [Status.Loading]: {
    classes:
      'border-slate-700 bg-slate-600 hover:bg-slate-700 active:bg-slate-800 focus:ring-slate-600',
    icon: LoaderCircleIcon,
    iconClass: 'animate-spin',
    text: 'Loading'
  },
  [Status.Online]: {
    classes:
      'border-emerald-700 bg-emerald-600 hover:bg-emerald-700 active:bg-emerald-800 focus:ring-emerald-600',
    icon: CircleCheckIcon,
    text: 'Online'
  },
  [Status.Offline]: {
    classes: 'border-red-700 bg-red-600 hover:bg-red-700 active:bg-red-800 focus:ring-red-600',
    icon: CircleXIcon,
    text: 'Offline'
  }
};
