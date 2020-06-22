<template>
  <div v-if="loading" id="loading">
    <v-progress-circular indeterminate size="100" width="10" color="#dddddd"/>
  </div>
  <v-app v-else>
    <toolbar :title="title" :primary="primary" />
    <v-content>
      <banner  :header="pageHeader" />
      <router-view id="router-view"/>
    </v-content>

    <Footer/>
  </v-app>
</template>

<script>
import Toolbar from '@/components/Toolbar';
import Banner from '@/components/Banner';
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
    Banner,
    Footer
  },

  data: () => ({
    loading: true,
    title: "loading...",
    primary: 'white',
    endpoint: process.env.VUE_APP_API_ENDPOINT,
    pageHeader: "Hello and Welcome"
  }),
  watch: {
    '$route'(to) {
      this.pageHeader = to.meta? to.meta.title : null;
    }
  }
};
</script>

<style scoped>
  main {
    padding-top:0px !important;
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