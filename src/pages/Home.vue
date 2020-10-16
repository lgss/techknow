<template>
  <v-container>
    <v-skeleton-loader v-if="loading" type="article" class="mt-8"/>
    <div v-else>
      <v-row>
        <v-col v-html="content">
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn role="button" color="success" id="btn-home-start-assessment" to="/select">Start</v-btn>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
  export default {
    name: 'home',
    data () {
      return {
        content: "",
        loading: true,
        endpoint: process.env.VUE_APP_API_ENDPOINT
      }
    },
    created() {
      fetch(this.endpoint + '/content/landing')
        .then(x => x.json())
        .then( x => {
          this.content = x.content
          this.loading = false
        })
  },
  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }
</style>
