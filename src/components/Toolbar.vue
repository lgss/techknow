<template>
    <v-app-bar app :color="primary" >
        <v-container fluid>
            <v-col class="d-flex justify-center">
                <a href="/" style="text-decoration:none">
                    <v-toolbar-title class="white--text">
                        <b>{{ title }}</b>
                    </v-toolbar-title>
                </a>
            </v-col>
        </v-container>
    </v-app-bar>
</template>

<script>
export default {
    props: ["title", "primary"]
};
</script>

<style scoped>
    .banner {
        background-color:#1D5F7A;
        margin-top:56px;
    }
</style>
