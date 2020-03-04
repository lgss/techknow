<template>
  <v-container>
    <v-row>
      <v-col>
        <h1 id="title">Welcome to <b>techKNOW</b></h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <p>TECHknow helps you with your independence.</p>
 
        <p>Choose what you want help with.
        Then answer the questions to find what you need.</p>
 
        <p>At the end, you will have a list of support options just for you. This list will include helpful things in Cambridgeshire and the UK like…</p>
        <br>Websites
        <br>Products
        <br>Activities
        <br>Contacts
        <br>
        <br>Have fun!
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn id="btn-home-start-assessment" to="/assess">Go to assessment</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'home',
    data () {
      return {
        msg: 'Welcome to Your Vue.js PWA'
      }
    }
  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #35495E;
  }
</style>
