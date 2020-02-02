<template>
  <v-app>
    <toolbar/>

    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import Toolbar from '@/components/Toolbar';

export default {
  name: 'App',

  components: {
    Toolbar,
  },

  data: () => ({
    //
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
</style>