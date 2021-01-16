<template>
  <v-app>
    <navbar v-if="getLoadingcomplete"/>
    <v-main>
      <v-container>
        <v-row justify="center" align="center">
          <v-col cols="12" align="center">
          </v-col>
        </v-row>
      </v-container>
      <router-view/>
    </v-main> 
  </v-app>
</template>

<script>
import navbar from './views/Navbar.vue'
import { mapGetters } from 'vuex'
import bottombar from './views/Bottombar.vue'
import RotateLoader from 'vue-spinner/src/RotateLoader.vue'

export default {
  name: 'app',
  components: { navbar, bottombar, RotateLoader },
  computed: {
    ...mapGetters(['getLoadingcomplete'])
  }
}
</script>

<style>
#app {
  font-family: Arial;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
