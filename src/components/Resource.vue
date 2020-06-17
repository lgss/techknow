<template>
    <v-card class="mx-auto resource">
        <v-card-text>
            <p class="display-1 text--primary">{{ $attrs.doc.name }}</p>
            <div class="text--primary">
                <span v-html="$attrs.doc.content"></span>
            </div>
            <div>
                <v-chip
                    v-for="iTag in $attrs.doc.includeTags"
                    :key="iTag"
                    class="ma-2"
                    color="green"
                    text-color="white"
                >
                    {{ iTag }}
                </v-chip>
                <v-chip
                    v-for="eTag in $attrs.doc.excludeTags"
                    :key="eTag"
                    class="ma-2"
                    color="red"
                    text-color="white"
                >
                    {{ eTag }}
                </v-chip>
            </div>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    name: "Resource",
};
</script>

<style scoped></style>
