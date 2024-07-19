export const prettifyDate = (date: Date, lang?: string) => {
  // lang can be set to undefined for a default locale
  return new Intl.DateTimeFormat(lang, {
    dateStyle: 'medium',
    timeStyle: 'medium'
  }).format(date);
};
