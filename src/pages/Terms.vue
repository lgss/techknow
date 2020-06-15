<template>
    <div>
        terms
    </div>
</template>

<style>

</style>

<script>
export default {
    name: "terms",
    data() {
        return {
            endpoint: process.env.VUE_APP_API_ENDPOINT
        }
    },
    created() {
        fetch(this.endpoint + '/config/terms')
    }
}
</script>

