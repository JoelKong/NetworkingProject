import { browser } from '$app/environment';

/**
 * Retrieves the preferred client language, or the `defaultLang` if not
 * specified or the requester is not from a browser context.
 */
export const getClientLanguage = (reqHeaders: Headers, defaultLang: string = 'en-US') => {
  if (browser) return navigator.language;

  return reqHeaders.get('Accept-Language')?.split(',')?.[0] ?? defaultLang;
};
