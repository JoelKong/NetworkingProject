export const prettifyDate = (date: Date) => {
  return new Intl.DateTimeFormat().format(date);
};
