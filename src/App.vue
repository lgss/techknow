<template>
  <div v-if="loading" id="loading">
    <v-progress-circular indeterminate size="100" width="10" color="#dddddd"/>
  </div>
  <v-app v-else>
    <toolbar :title="title" :primary="primary" />

    <v-content>
      <router-view/>
    </v-content>

    <Footer/>
  </v-app>
</template>

<script>
import Toolbar from '@/components/Toolbar';
import Footer from '@/components/Footer';
import landing from '@/js/landing.js';

export default {
  name: 'App',
  created() {
    fetch(this.endpoint + '/config/general')
      .then(x => x.json())
      .then( x => {
        document.title = x.title
        this.title = x.title
        landing.set(x.landing)
        this.primary = x.primary
        this.$vuetify.theme.primary = x.primary
        this.loading = false
      })
  },

  components: {
    Toolbar,
    Footer
  },

  data: () => ({
    loading: true,
    title: "loading...",
    primary: 'white',
    endpoint: process.env.VUE_APP_API_ENDPOINT
  }),
};
</script>

<style scoped>
  main {
    text-align: center;
    margin-top: 40px;
    margin-left: 20px;
    margin-right: 20px;
  }

  #loading {
    text-align: center;
    padding-top: 30vh;
  }
</style>