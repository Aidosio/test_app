<template>
  <section class="hero is-danger mt-4">
    <div class="hero-body">
      <p class="title">
        Разделы
      </p>
    </div>
  </section>
  
  <div class="container is-fluid" v-for="section in sections" :key="section.id">
    <div class="box mt-4">
      <article class="media">
        <div class="media-left">
          <figure class="image">
            <img :src="section.get_thumbnail" alt="Image">
          </figure>
        </div>
        <div class="media-content">
          <div class="content">
            <p>
              <strong>{{ section.name }}</strong>
              <br>
              <span class="section-content">{{ section.content }}</span>
            </p>
          </div>
          <nav class="level is-mobile">
            <router-link :to="{
              name: 'SectionsPage',
              params: {
                id: section.id
              }
            }" class="button is-primary">Подробнее</router-link>
          </nav>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Sections",
  data() {
    return {
      sections: []
    }
  },
  created() {
    axios.get('/api/v1/sections/').then(response => {
      this.sections = response.data
    })
  }
}
</script>

<style lang="scss" scoped>
.image {
  img {
    width: 200px;
    height: 120px;
    object-fit: cover;
  }
}

.section-content {
  margin: 0;
  -webkit-line-clamp: 2;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

@media screen and (max-width: 500px) {
  .media {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
}
</style>