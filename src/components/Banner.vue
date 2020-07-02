<template>
        <v-row class="banner primary">    
            <v-col class="d-flex align-center justify-center">
                <h1 class="text-h1 white--text">
                    {{header}}
                </h1>
            </v-col>
        </v-row>
</template>

<script>
export default {
    props: ["header"]
};
</script>

<style scoped>
    .banner {
        margin-top:56px;
        min-height: 150px;
    }
</style>
