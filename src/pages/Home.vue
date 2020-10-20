<template>
  <v-container>
    <div v-if="loading" class="loading">
      <v-progress-circular indeterminate size="100" width="10" color="#dddddd"/>
    </div>
    <v-row>
      <v-col v-html="content">
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn role="button" color="success" id="btn-home-start-assessment" to="/select">Start</v-btn>
      </v-col>
    </v-row>
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