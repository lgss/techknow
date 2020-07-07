<template>
    <v-app-bar app shrink-on-scroll prominent :color="this.$vuetify.theme.primary">
        <div class="d-flex flex-column align-center">
            <a href="/" style="text-decoration:none">
                <v-toolbar-title class="white--text">
                    <b>{{ title }}</b>
                </v-toolbar-title>
            </a>
            <h3 class="white--text subheader">
                {{header}}
            </h3>
        </div>
    </v-app-bar>
</template>

<script>
export default {
    props: ["title", "header"]
};
</script>

<style scoped>
    div {
        width: 100%
    }
    
    .v-app-bar--is-scrolled .subheader {
        display: none;
    }
</style>