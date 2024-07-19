export interface SensorDashboardCardProps {
  klass: string;
  lastUpdated: Date;
  temperatureData: number[];
  humidityData: number[];

  formatDate?: (date: Date) => string;
}
