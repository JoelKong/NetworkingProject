import { getClientLanguage } from '$lib/utils/i18n/localize';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ request }) => {
  return {
    client: {
      lang: getClientLanguage(request.headers)
    }
  };
};
