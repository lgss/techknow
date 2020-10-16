<template>
  <v-app v-if="loadFailed">
    <v-dialog
      persistent
      max-width="290"
      :value="true"
    >
    <v-card>
        <v-card-title class="headline">
          Something went wrong
        </v-card-title>
        <v-card-text><p>There was a problem loading the site.</p><p> Check your internet and try again or contact us if the problem continues.</p></v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="reload()"
          >
            Try again
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
  <div v-else-if="loading" id="loading">
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

export default {
  name: 'App',
  created() {
    fetch(this.endpoint + '/theme')
      .then(x => x.json())
      .then( x => {
        document.title = x.title
        this.title = x.title
        this.$vuetify.theme.themes.light.primary = x.primary
        this.$vuetify.theme.themes.light.secondary = x.secondary
        this.loading = false
      })
      .catch(err => {
          this.loadFailed = true
          console.error(err)
        }
      )
  },
  components: {
    Toolbar, 
    Footer
  },
  
  data: () => ({
    loading: true,
    loadFailed: false,
    title: "loading...",
    endpoint: process.env.VUE_APP_API_ENDPOINT
  }),
  computed: {
    pageTitle() {return this.$route.meta ? this.$route.meta.title : ''}
  },
  methods: {
    reload() {
      window.location.reload();
    }
  }
};
</script>

<style>
  main {
    background-color: #f7f7f7;
  }

  #router-view {
    margin-left: auto;
    margin-right: auto;
  }

  #loading {
    text-align: center;
    padding-top: 30vh;
  }
  
  .v-btn:focus{
      outline: -webkit-focus-ring-color auto 1px;
  }
  
  .v-card__title {
    word-break:normal !important;
  }

  .v-card__subtitle, .v-card__text {
    font-size: 1.2rem;
  }
</style>