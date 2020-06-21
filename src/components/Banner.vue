<template>
        <v-row class="banner">    
            <v-col class="d-flex align-center justify-center">
                <h1 :class="text-h1" class="white--text">
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
        background-color:#1D5F7A;
        margin-top:56px;
        min-height: 150px;
    }
</style>
