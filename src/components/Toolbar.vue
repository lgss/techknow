<template>
    <v-app-bar color="primary" app shrink-on-scroll prominent>
        <v-container class="d-flex flex-column align-center">
            <router-link to='/'>
                <v-toolbar-title class="white--text">
                    <div role="heading" aria-level="1" class="font-weight-black">{{ title }}</div>
                </v-toolbar-title>
            </router-link>
            <v-container class="d-flex flex-column align-center">
                <h2 role="heading" aria-level="2" tabindex="0" class="white--text subheader">
                    {{header}}
                </h2>
            </v-container>
        </v-container>

    </v-app-bar>
</template>

<script>
export default {
    props: ["title", "header"]
};
</script>

<style scoped>    
    .v-app-bar--is-scrolled .subheader {
        display: none;
    }
</style>
