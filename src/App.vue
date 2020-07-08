<template>
  <div v-if="loading" id="loading">
    <v-progress-circular indeterminate size="100" width="10" color="#dddddd"/>
  </div>
  <v-app v-else>
    <toolbar :title="title" :header="pageTitle" />
    <v-main>
      <v-container fluid>
        <router-view id="router-view"/>
      </v-container>
    </v-main>
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
    endpoint: process.env.VUE_APP_API_ENDPOINT
  }),
  computed: {
    pageTitle() {return this.$route.meta ? this.$route.meta.title : ''}
  }
};
</script>

<style scoped>
  main {
    background-color: #f7f7f7;
  }

  #router-view {
    text-align: center;
    margin-top: 40px;
    margin-left: auto;
    margin-right: auto;
  }

  #loading {
    text-align: center;
    padding-top: 30vh;
  }
</style>