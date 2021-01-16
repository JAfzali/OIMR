<template>
  <container fluid>
    <div>
      <v-btn @click="first" icon color="blue">
              <v-icon>first_page</v-icon>
        </v-btn>
      <v-btn @click="prev" icon color="blue">
              <v-icon>chevron_left</v-icon>
        </v-btn>
        <v-btn @click="next" icon color="blue">
                <v-icon>chevron_right</v-icon>
          </v-btn>
          <v-btn @click="last" icon color="blue">
                  <v-icon>last_page</v-icon>
            </v-btn>
      {{currentPage}}/{{totalPages}}
    </div>
    <div  style="text-align: left;" class= "display-2 font-weight-thick">Racks</div>
    <div v-for="post in filteredPosts" class="posts" :key="post">
    <v-row
    >
      <v-col
        cols="12"
        md="12"
      >
      </v-col>
    </v-row>
    <v-row
    class="grey lighten-5"
    >
      <v-col
        cols="12"
        md="3"
      >
      <v-card
      class="mx-auto text-center"
      outlined
      width="300px"
  >
        <v-list dense flat>
          <v-subheader >Rack info</v-subheader>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
            v-for="(value, key) in post[1]" :key="key"
          >
          <v-list-item-content>
            <v-list-item-title>{{key}}</v-list-item-title>
          </v-list-item-content>
            <v-spacer></v-spacer>
            <v-list-item-content>
              <v-list-item-subtitle>
          {{value}}
        </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-card>
      </v-col>
      <v-col
        cols="12"
        md="8"
      >
      <v-card>
        <table>
          <tr v-for="list in post[0]"
          :key="list">
          <td
            v-for="pipe in list"
            :key="pipe.Serial_Number"
            >
            <v-tooltip top>
              <template v-slot:activator="{ on, attrs }">
                <v-btn v-if="getDateDiff(pipe) < 17" v-bind="attrs" v-on="on" color="green" fab x-small
                >
                  <span class="black--text ">{{pipe.Position}}</span>
                </v-btn>
                <v-btn v-else-if="getDateDiff(pipe) < 62 & getDateDiff(pipe) >= 18" v-bind="attrs" v-on="on" color="yellow" fab x-small
                >
                  <span class="black--text ">{{pipe.Position}}</span>
                </v-btn>
                <v-btn v-else v-on="on" color="red" fab x-small
                >
                  <span class="black--text ">{{pipe.Position}}</span>
                </v-btn>
              </template>
              <h1><b>{{pipe.Position}}</b></h1>
              <br>
            <div><b>Serial Number:</b> {{pipe.Serial_Number}}</div>
            <div><b>Item Number:</b> {{pipe.Item_No}}</div>
            <div><b>Inspection Date:</b> {{pipe.Date_Inspected}}</div>
            <div><b>Description:</b> {{pipe.Description}}</div>

            </v-tooltip>
          </td>
        </tr>
        </table>
      </v-card>
      </v-col>
    </v-row>
    <h3 v-for="postpost in post[0]" :key="postpost"></h3>
    </div>
  </container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import moment from 'moment'
export default {
  name: 'test',
  data () {
    return {
      currentPage: 1,
      postsPerPage: 1,
      posts: [],
      posts123: {
        20: {
          title: 'example post 1',
          date: 'Oct 30',
          body: 'some text'
        },
        48: {
          title: 'example post 2',
          date: 'Oct 30',
          body: 'some text'
        },
        36: {
          title: 'example post 3',
          date: 'Oct 30',
          body: 'some text'
        },
        22: {
          title: 'example post 4',
          date: 'Oct 30',
          body: 'some text'
        },
        55: {
          title: 'example post 5',
          date: 'Oct 30',
          body: 'some text'
        },
        88: {
          title: 'example post 6',
          date: 'Oct 30',
          body: 'some text'
        },
        23: {
          title: 'example post 7',
          date: 'Oct 30',
          body: 'some text'
        }
      },
      items: [
        { text: 'Site', value: 'Kverneland' },
        { text: 'Site Location', value: 'Rig_Ready' },
        { text: 'Rack ID', value: '01A' },
        { text: 'Item Number', value: 'OWS278DP.01' },
        { text: 'Description', value: 'N/A' },
        { text: 'Maxrowcount', value: '20' }
      ]
    }
  },
  computed: {
    ...mapGetters([
      'getUsername', 'getAdminRacks'
    ]),
    allPosts () {
    	return Object.keys(this.$store.getters.getAdminRacks).map(pid => this.$store.getters.getAdminRacks[pid]) // eslint-disable-line
    },
  	filteredPosts () { // eslint-disable-line
      return this.allPosts.slice((this.currentPage - 1) * this.postsPerPage, this.currentPage * this.postsPerPage)
    },
		totalPages () { // eslint-disable-line
    	return Math.ceil(this.allPosts.length / this.postsPerPage)// eslint-disable-line

    }, // eslint-disable-line
    allItems () {
      return this.items
    }
  },
  created: function () {
    this.fetchAdminRacks()
  },
  methods: {
    ...mapActions(['fetchAdminRacks']),
    next () {
    	if ( this.currentPage < this.totalPages) { // eslint-disable-line
      	this.currentPage++ // eslint-disable-line
      }
    },
    prev () {
    	if (this.currentPage > 1) { // eslint-disable-line
      	this.currentPage-- // eslint-disable-line
      }
    },
    first () {
      if (this.currentPage > 1) { // eslint-disable-line
       this.currentPage = 1 // eslint-disable-line
      }
    },
    last () {
      if (this.currentPage < this.totalPages) { // eslint-disable-line
       this.currentPage = this.totalPages // eslint-disable-line
      }
    },
    getDateDiff: function (pipe) {
      var now = moment(new Date())
      var end = moment(pipe.Date_Inspected)
      var duration = moment.duration(now.diff(end))
      var days = duration.asDays()
      console.log(days)
      return days
    }
  }
}
</script>

<style lang="css" scoped>

h1, h2 {
  font-weight: bold
}

ul {
  list-style-type: none;
  padding: 0
}
li {
  display: inline-block;
  margin: 0 10px
  }

.paginate-list {
  width: 159px;
  margin: 0 auto;
  text-align: left
}
  li {
    display: block;
    }
.paginate-links.items {
  user-select: none
}
  a {
    cursor: pointer
  }

  li.active a {
    font-weight: bold
}
  li.next:before {
    margin-right: 13px;
    color: #ddd;
}
  li.disabled a {
    color: #ccc;
    cursor: no-drop
}
a {
  color: #42b983
}
.v-btn{
    margin:0px;
}
#bigbtn {
  background-color: var(--secondary-color);
}
table { margin: auto; }

table, tr, td {
  border: 1px solid black;
}

.v-card {
  overflow-y:auto;
  overflow-x:auto;
}
</style>
