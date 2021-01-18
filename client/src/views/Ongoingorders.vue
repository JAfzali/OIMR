<template>
  <v-container fluid>
    <!-- Stack the columns on mobile by making one full-width and the other half-width -->
    <v-row class="white">
      <v-col cols="1" md="12">
        <v-card class="white" elevation="0" tile>
          <v-row align="center" class="lightbox black--text pa-0 fill-height">
          </v-row>
          <v-row align="center" class="lightbox black--text pa- fill-height">
            <v-col>
              <div style="color: #204060" class="display-1">
                <b>{{ getUsername }}</b>
              </div>
              <div style="color: #204060" class="display-0">{{ getAsset }}</div>
            </v-col>
          </v-row>
          <v-divider class="mx-0" color="white"></v-divider>
        </v-card>
      </v-col>
    </v-row>

    <!-- Columns are always 50% wide, on mobile and desktop -->
    <v-row class="white">
      <v-col cols="6">
        <v-card class="pa-10" outlined tile>
          <h2>Orders</h2>
          <br />
          <v-data-table
            to="/orderconfirm"
            height="250"
            :loading="commonload"
            :headers="header_order"
            :items="filterOrders"
            :items-per-page="5"
            class="elevation-1"
          >
            <template v-slot:item.action="{ item }">
              <v-btn dark x-small text color="black" @click="getOrderPDF(item)">
                <v-icon>description</v-icon>
              </v-btn>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-card class="pa-10" outlined tile>
          <h2>Inspection</h2>
          <br />
          <v-data-table
            height="250"
            :loading="commonload"
            :headers="header1"
            :items="filterInspection"
            :items-per-page="5"
            class="elevation-1"
          >
            <template v-slot:item.action="{ item }">
              <v-btn v-if="item.Equipment == 'Drill Pipe'" dark x-small text color="black" @click="getdpPDF(item)">
                <v-icon>description</v-icon>
              </v-btn>
              <v-btn v-else-if="item.Equipment == 'Heavy Weight'" dark x-small text color="black" @click="gethwPDF(item)">
                <v-icon>description</v-icon>
              </v-btn>
              <v-btn v-else-if="item.Equipment == 'Drill Collar'" dark x-small text color="black" @click="getdcPDF(item)">
                <v-icon>description</v-icon>
              </v-btn>
            </template>
            <template v-slot:item.action1="{ item }">
              <v-btn v-if="item.Equipment == 'Drill Pipe'" dark x-small text color="black" @click="getExcel(item)">
                <v-icon>mdi-file-excel</v-icon>
              </v-btn>
              <v-btn v-else-if="item.Equipment == 'Heavy Weight'" dark x-small text color="black" @click="getExcelhw(item)">
                <v-icon>mdi-file-excel</v-icon>
              </v-btn>
              <v-btn v-else-if="item.Equipment == 'Drill Collar'" dark x-small text color="black" @click="getExceldc(item)">
                <v-icon>mdi-file-excel</v-icon>
              </v-btn>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-card class="pa-10" outlined tile>
          <h2>Machining</h2>
          <br />
          <v-data-table
            height="250"
            :loading="commonload"
            :headers="header2"
            :items="filterMachining"
            :items-per-page="5"
            class="elevation-1"
          >
          <template v-slot:item.action="{ item }">
              <v-btn
                v-if="item.Equipment == 'Drill Pipe'"
                dark
                x-small
                text
                color="black"
                @click="getMachExcel(item)"
              >
                <v-icon>mdi-file-excel</v-icon>
              </v-btn>
              <v-btn
                v-else-if="item.Equipment == 'Heavy Weight'"
                dark
                x-small
                text
                color="black"
                @click="getMachExcelHW(item)"
              >
                <v-icon>description</v-icon>
              </v-btn>
              <v-btn
                v-else-if="item.Equipment == 'Drill Collar'"
                dark
                x-small
                text
                color="black"
                @click="getMachExcelDC(item)"
              >
                <v-icon>info</v-icon>
              </v-btn>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-card class="pa-10" outlined tile>
          <h2>Hardbanding</h2>
          <br />
          <v-data-table
            :loading="commonload"
            height="250"
            :headers="header2"
            :items="filterHardbanding"
            :items-per-page="5"
            class="elevation-1"
          >
            <template v-slot:item.action="{ item }">
              <v-btn
                v-if="item.Equipment == 'Drill Pipe'"
                dark
                x-small
                text
                color="black"
                @click="getHardExcel(item)"
              >
                <v-icon>mdi-file-excel</v-icon>
              </v-btn>
              <v-btn
                v-else-if="item.Equipment == 'Heavy Weight'"
                dark
                x-small
                text
                color="black"
                @click="getHardExcelHW(item)"
              >
                <v-icon>mdi-file-excel</v-icon>
              </v-btn>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import axios from "axios";
export default {
  name: "completedorders",
  props: {
    source: String
  },
  data() {
    return {
      commonload: false,
      header1: [
        {
          text: "Order nr",
          align: "start",
          sortable: true,
          value: "Order_No"
        },
        { text: "Inspection date", value: "Return_Date" },
        { text: "Item no", value: "Item_No" },
        { text: "Equipment", value: "Equipment" },
        { text: "Qty", value: "QTY_Recived" },
        { text: "PDF", value: "action", sortable: false },
        { text: "Excel", value: "action1", sortable: false }
      ],
      header_order: [
        {
          text: "Order nr",
          align: "start",
          sortable: true,
          value: "Order_No"
        },
        { text: "Order date", value: "Return_Date" },
        { text: "Item no", value: "Item_No" },
        { text: "Equipment", value: "Equipment" },
        { text: "Qty", value: "QTY_Recived" },
        { text: "PDF", value: "action", sortable: false }
      ],
      header2: [
        {
          text: "Order nr",
          align: "start",
          sortable: true,
          value: "Order_No"
        },
        { text: "Inspection date", value: "Return_Date" },
        { text: "Item no", value: "Item_No" },
        { text: "Equipment", value: "Equipment" },
        { text: "Excel", value: "action", sortable: false }
      ],
      orders: [],
      insp: [
        {
          name: "10404",
          calories: "02/10/2020",
          fat: "Saipem",
          carbs: "SC8800DC.01",
          protein: "Drill Collar",
          iron: "3"
        },
        {
          name: "10403",
          calories: "02/10/2020",
          fat: "Saipem",
          carbs: "SC8434DC.01",
          protein: "Drill Collar",
          iron: "1"
        },
        {
          name: "10402",
          calories: "02/10/2020",
          fat: "Saipem",
          carbs: "SC8512DP.01",
          protein: "Drill Pipe",
          iron: "1"
        },
        {
          name: "10254",
          calories: "24/06/2020",
          fat: "Saipem",
          carbs: "SC8800DC.01",
          protein: "Drill Collar",
          iron: "124"
        }
      ],
      mach: [],
      hard: []
    };
  },
  methods: {
    getdpPDF(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getdpPDF", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    gethwPDF(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/gethwPDF", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getdcPDF(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getdcPDF", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getExcel(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getdpExcel", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.excellink, "_blank");
        });
    },
    getExcelhw(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/gethwExcel", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.excellink, "_blank");
        });
    },
    getExceldc(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getdcExcel", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.excellink, "_blank");
        });
    },
    getOrderPDF(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getOrderPDF", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getMachExcel(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getMachExcel", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.excellink, "_blank");
        });
    },
    getMachExcelHW(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getMachExcelHW", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.excellink, "_blank");
        });
    },
    getMachExcelDC(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getMachExcelDC", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.excellink, "_blank");
        });
    },
    getHardExcel(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getHardExcel", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.excellink, "_blank");
        });
    },
    getHardExcelHW(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getHardExcelHW", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.excellink, "_blank");
        });
    }
  },
  mounted() {
    this.commonload = true;
    axios
      .get("/getOrderconfirm", {
        params: { username: this.$store.getters.getUsername }
      })
      .then(response => {
        console.log(response);
        this.orders = response.data;
        this.commonload = false;
      });
  },
  computed: {
    ...mapGetters([
      "getEmail",
      "getUsername",
      "getAssetlist",
      "getAsset",
      "getFleet"
    ]),
    isAssetList() {
      if (this.getAssetlist.length > 0) {
        return true;
      } else {
        return false;
      }
    },
    filterOrders() {
      if (this.getFleet === true) {
        return this.orders.filter(order => {
          return order.Completed === "No";
        });
      } else {
        return this.orders.filter(order => {
          return order.Completed === "No" && order.Asset === this.getAsset;
        });
      }
    },
    filterInspection() {
      if (this.getFleet === true) {
        return this.orders.filter(order => {
          return order.Check_Inspection === "No";
        });
      } else {
        return this.orders.filter(order => {
          return (
            order.Check_Inspection === "No" && order.Asset === this.getAsset
          );
        });
      }
    },
    filterMachining() {
      if (this.getFleet === true) {
        return this.orders.filter(order => {
          return order.Check_Machining === "No";
        });
      } else {
        return this.orders.filter(order => {
          return (
            order.Check_Machining === "No" && order.Asset === this.getAsset
          );
        });
      }
    },
    filterHardbanding() {
      if (this.getFleet === true) {
        return this.orders.filter(order => {
          return order.Check_Hardbanding === "No";
        });
      } else {
        return this.orders.filter(order => {
          return (
            order.Check_Hardbanding === "No" && order.Asset === this.getAsset
          );
        });
      }
    }
  }
};
</script>

<style lang="css" scoped>
.inline {
  display: inline-block;
  margin-right: 10px;
}
</style>