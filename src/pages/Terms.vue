<template>
    <div>
        <v-progress-circular id="loading-terms" v-if="loading"></v-progress-circular>
        <div v-else-if="terms" class='text-left'>
            <h1>Terms and Conditions</h1>
            <div id='terms-content' class='text-left'>
                {{terms}}
            </div>
        </div>
        <div v-else>We're sorry, but we're unable to find this at the moment.</div>
    </div>
</template>

<style>
.terms-content {

}

</style>

<script>
export default {
    name: "terms",
    data() {
        return {
            endpoint: process.env.VUE_APP_API_ENDPOINT,
            terms: null,
            loading: true
        }
    },
    created() {
        fetch(this.endpoint + '/config/disclaimer')
        .then(x=>x.json())
        .then(x=>{
            this.terms = x;
        })
        .catch()
        .finally(()=>this.loading = false)
    }
}
</script>

