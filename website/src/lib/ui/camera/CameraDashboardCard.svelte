<script lang="ts">
  import VideoOffIcon from 'lucide-svelte/icons/video-off';
</script>

<section
  class="rounded bg-lime-200 p-3 flex flex-col gap-3 border border-lime-400 md:col-span-full"
>
  <figure class="flex flex-col gap-2 rounded">
    <figcaption class="text-2xl">Camera Feed</figcaption>
    <div class="flex place-content-center p-10 border border-black rounded">
      <VideoOffIcon size={48} />
    </div>
  </figure>
</section>
