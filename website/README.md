# Watering Can Frontend

Frontend site for the watering can project for INF1006 - Computer Networks.

## Building/running

### Pre-requisites

It is recommended to use [pnpm](https://pnpm.io/) for Node.js package management.

Follow the [instructions to install pnpm on their website](https://pnpm.io/installation).

---

### Steps

1. Clone the project locally
2. Start the backend server
3. Install the dependencies with `pnpm i`
4. Uncomment or add the following lines to the [Vite config](./vite.config.ts):

    ```ts
    export default defineConfig({
      // ...[Other config]...
      server: {
        proxy: {
          '/api': {
            target: 'http://192.168.1.10:5000',
            changeOrigin: true,
            rewrite: (path) => path.replace(/^\/api/, '')
          }
        }
      }
    })
    ```

    This adds a proxy to the `/api` route that the code uses such that it correctly
    calls the backend endpoints.
5. Run the application with `pnpm dev`.

    Alternatively, the app can be built with `pnpm build`, where
    the resulting built app will be outputted to the dist/ folder. This will then
    require a local development server such as the `http.server` Python 3 module
    if not uploaded to an existing web server.

## Project structure

This project uses a [standard](https://kit.svelte.dev/docs/project-structure)
[SvelteKit](https://kit.svelte.dev) setup.

New client/server-side routes are to be added in the `src/routes` folder, and
the logic is to be added in the `src/lib` folder, where it can then be imported
via [`$lib`](https://kit.svelte.dev/docs/modules#$lib).
