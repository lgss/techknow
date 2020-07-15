<template>
  <v-container>
    <v-row>
      <v-col v-html="landing">
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn role="button" id="btn-home-start-assessment" to="/select">Go to assessment</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import landing from '@/js/landing.js'
  import newTab from '@/js/newTab.js'
  export default {
    name: 'home',
    data () {
      return {
        landing: newTab(landing.get())
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
