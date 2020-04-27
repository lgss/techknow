<template>
    <v-app-bar app :color="primary">
        <a href='/' style="text-decoration:none"><v-toolbar-title class="white--text"><b>{{title}}</b></v-toolbar-title></a>
        <v-spacer/>
    </v-app-bar>
</template>

<script>
export default {
    props: ['title', 'primary']
}
</script>