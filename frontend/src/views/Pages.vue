<template>
  <section class="hero is-info mt-4">
    <div class="hero-body">
      <p class="title">
        {{ content.name }}
      </p>
    </div>
  </section>
  <div class="container is-fluid">
    <img class="mt-4" :src="content.get_image">
    <div class="content mt-4">
      <p>{{ content.content }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Pages",
  data() {
    return {
      content: []
    }
  },
  watch: {
    '$route.params.id': {
      immediate: true,
      handler() {
        axios.get(`/api/v1/pages/${this.$route.params.id}`).then(response => {
          this.content = response.data
        })
      },
    },
  },
}
</script>

<style scoped>
img {
  width: 30%;
  height: 400px;
  object-fit: cover;
}

@media screen and (max-width: 1023px) {
  img {
    width: 100%;
    height: 400px;
    object-fit: cover;
  }
}
</style>