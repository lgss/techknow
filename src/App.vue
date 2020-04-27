<template>
  <div v-if="loading" id="loading">
    <v-progress-circular indeterminate size="100" width="10" color="#dddddd"/>
  </div>
  <v-app v-else>
    <toolbar :title="title" :primary="primary" />

    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import Toolbar from '@/components/Toolbar';
import landing from '@/js/landing.js';

export default {
  name: 'App',
  created() {
    fetch('https://nngfac1fjl.execute-api.eu-west-2.amazonaws.com/dev/config/general')
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
    Toolbar
  },

  data: () => ({
    loading: true,
    title: "loading...",
    primary: 'white'
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