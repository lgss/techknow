<template>
  <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">Name</th>
          <th class="text-left">Content</th>
          <th class="text-left">Tags</th>
          <th class="text-left">Filter check</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="resource in results.resources.filter(resource => resource.tags.some(tag => filterTags.some(x => x === tag)))" :key="resource.name">
          <td class="text-left">{{ resource.name }}</td>
          <td class="text-left">{{ resource.content }}</td>
          <td class="text-left">{{ resource.tags }}</td>
          <td class="text-left">{{ resource.tags.some(tag => filterTags.some(x => x === tag)) }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
export default {
    name: 'Result',
    components: {},
    props: ["results"],
    data(){
        return {
          filterTags: ['tag3','tag4']
        }
    }
}
</script>

<style>

</style>