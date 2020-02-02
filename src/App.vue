<template>
  <v-app>
    <toolbar/>

    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import AppToolbar from '@/components/AppToolbar';

export default {
  name: 'App',

  components: {
    AppToolbar,
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