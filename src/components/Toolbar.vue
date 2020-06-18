<template>
    <v-app-bar :extended="isExtended" prominent app :color="primary" >
        <!-- <v-container class="d-flex justify-center"> -->
        <v-container fluid>
            <v-col class="d-flex justify-center">
                <a href="/" style="text-decoration:none">
                    <v-toolbar-title class="white--text">
                        <b>{{ title }}</b>
                    </v-toolbar-title>
                </a>
            </v-col>
            <v-divider/>
            <v-col v-if="isExtended" class="d-flex justify-center">
                <h1 class="page-title white--text">
                    {{header}}
                </h1>
            </v-col>

        </v-container>
    </v-app-bar>
</template>

<script>
export default {
    props: ["title", "primary", "header"],
    computed: {
        isExtended() {
            return !!this.header;
        }
    }
};
</script>

<style scoped></style>
