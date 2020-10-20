<template>
  <v-container>
    <v-row>
      <v-col>
        <v-banner two-line v-model="showConsent">
          <v-avatar slot="icon" color="primary">
            <v-icon color="white">
              mdi-lock
            </v-icon>
          </v-avatar>
          <span>
            This website uses cookies, is this ok?
          </span>
          <template v-slot:actions>
            <v-btn @click="setConsent(false)">
              Dismiss
            </v-btn>
            <v-btn @click="setConsent(true)" color="primary">
              Accept
            </v-btn>
          </template>
        </v-banner>
      </v-col>
    </v-row>  
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
        showConsent: !localStorage.ga_consent,
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
    methods: {
      setConsent(enableConsent) {
        this.showConsent = false
        localStorage.ga_consent = enableConsent
        if (enableConsent)
          this.$ga.enable()
        else
          this.$ga.disable()
      }
    }
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
