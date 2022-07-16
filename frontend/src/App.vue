<script>
import axios from "axios";

export default {
  name: "App",

  data() {
    return {
      isActive: false,
      isDropActive: true,
      pages: {},
      sections: {},
    }
  },

  mounted() {
    axios.get('/api/v1/pages/').then(response => {
      this.pages = response.data
    })
    axios.get('api/v1/sections/').then(response => {
      this.sections = response.data
    })
  },

  methods: {}
}
</script>


<template>
  <div class="container is-fluid">
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <router-link class="navbar-item" to="/">
          <button class="button is-primary">AIDOS</button>
        </router-link>

        <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" @click="isActive = !isActive"
           data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu" :class="{active : isActive}">
        <div class="navbar-start">

          <div class="is-flex" v-for="page in pages" :key="page.id">
            <router-link :to="page.get_absolute_url" class="navbar-item">
              {{ page.name }}
            </router-link>
          </div>

          <div class="navbar-item has-dropdown is-hoverable" @click="isDropActive = !isDropActive">
            <router-link to="/sections" class="navbar-link">
              Разделы
            </router-link>

            <div class="navbar-dropdown" :class="{dropActive : isDropActive}">
              <router-link :to="{
                name: 'SectionsPage',
                params: {
                  id: section.id
                }
              }" class="navbar-item"
               v-for="section in sections" :key="section.id"
              >
                {{ section.name }}
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>

  <router-view/>
</template>

<style lang="scss">
@import "../node_modules/bulma";

@media screen and (max-width: 1023px) {
  .active {
    display: block;
  }

  .dropActive {
    display: none;
  }
}


</style>
