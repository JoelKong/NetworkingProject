<script lang="ts">
  import { Popover } from 'bits-ui';
  import XIcon from 'lucide-svelte/icons/x';

  import { intlFormatDistance } from 'date-fns';

  import StatusChip from '$lib/components/status/StatusChipContent.svelte';

  import ActionsDashboardCard from '$lib/ui/actions/ActionsDashboardCard.svelte';
  import CameraDashboardCard from '$lib/ui/camera/CameraDashboardCard.svelte';
  import SensorDashboardCard from '$lib/ui/sensors/SensorDashboardCard.svelte';

  import SettingsButton from '$lib/ui/settings/SettingsButton.svelte';

  import { flyAndScale } from '$lib/utils/transitions/fly-and-scale';

  import { getData } from '$lib/api/data';
  import { Status, statuses } from '$lib/data/status';
  import { activateSensors } from '$lib/api/modify';
  import { nextRandom } from '$lib/utils/math/random';

  import {
    humiditySensor,
    temperatureSensor,
    addHumidity,
    addTemperature
  } from '$lib/data/sensors';

  import { settings } from '$lib/data/settings';

  let date = $state(new Date());

  let intervalMs = $derived($settings.intervalMs); // Every 3 seconds

  let status = $state(Status.Loading);

  const getStatusData = (status: Status) => statuses[status];

  const onActivateSensorsClick = () => {
    activateSensors()
      .then((d) => d.json())
      .then((t) => {
        console.log(t);
      })
      .catch((e) => {
        console.log('Could not activate sensors:', e);
      });
  };

  const formatRelative = (date: Date, currDate: Date = new Date()) =>
    intlFormatDistance(date, currDate);

  let currDate = $state(new Date());
  let lastUpdated = $derived(formatRelative(date, currDate));

  $effect(() => {
    const tick = setInterval(() => {
      currDate = new Date();
    }, 1000);

    return () => clearInterval(tick);
  });

  $effect(() => {
    const result = setInterval(() => {
      date = new Date();
      getData()
        .then((j) => {
          status = Status.Online;
          console.log('Data retrieved:', j);

          addHumidity(j.humidity);
          addTemperature(j.temperature);
        })
        .catch((e) => {
          status = Status.Offline;

          console.error('Could not load data:', e);

          // Add mock data
          // TODO: Remove
          addHumidity(nextRandom(0, 100));
          addTemperature(nextRandom(20, 40));
        });
    }, intervalMs);

    return () => clearInterval(result);
  });
</script>

<header class="bg-sky-300 p-3 flex gap-3">
  <h1 class="font-semibold text-xl mr-auto">Watering Can</h1>
  <Popover.Root>
    <Popover.Trigger
      class="rounded border text-white px-2 flex items-center gap-2 transition-all focus:ring focus-visible:outline-none {getStatusData(
        status
      ).classes}"
      ><StatusChip {status} />
    </Popover.Trigger>
    <Popover.Content
      class="z-30 w-full max-w-[328px] rounded-xl border border-slate-300 bg-slate-100 shadow-md"
      transition={flyAndScale}
      sideOffset={8}
    >
      <header class="flex gap-2 items-center border-b border-slate-700 rounded-t-xl p-3 bg-white">
        <h3 class="text-lg font-bold mr-auto">Status</h3>
        <Popover.Close
          class="hover:bg-sky-200 active:bg-sky-300 rounded-full border border-sky-400 focus:ring focus-visible:outline-none focus:ring-sky-500 transition-all p-2"
        >
          <XIcon />
        </Popover.Close>
      </header>
      <main class="p-3 flex flex-col gap-2">
        <p class="text-sm">
          <em
            >Last updated at <time datetime={date.toISOString()}>{lastUpdated}</time>, refreshes
            every {intervalMs / 1000} seconds</em
          >
        </p>
      </main>
    </Popover.Content>
  </Popover.Root>

  <SettingsButton />
</header>

<main class="grid md:grid-cols-3 auto-cols-auto gap-6 m-6">
  <!-- Sensor data -->
  <SensorDashboardCard
    klass="md:col-span-2"
    lastUpdated={date}
    temperatureData={$temperatureSensor}
    humidityData={$humiditySensor}
  />

  <!-- Actions -->
  <ActionsDashboardCard {onActivateSensorsClick} />

  <!-- Camera feed -->
  <CameraDashboardCard />
</main>
