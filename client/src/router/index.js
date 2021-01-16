import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import firebase from 'firebase'
import Navbar from '../views/Navbar.vue'
import Racklocation from '../views/Racklocation.vue'
import Test from '../views/Test.vue'
import Racks from '../views/Racks.vue'
import Inventory from '../views/Inventory.vue'
import store from '../store'
import Orderconfirm from '../views/Orderconfirm.vue'
import Received from '../views/Received.vue'
import Preinvoice from '../views/PreInvoice.vue'
import Delivery from '../views/Delivery.vue'
import DrillPipe from '../views/dp.vue'
import HeavyWeight from '../views/hw.vue'
import DrillCollar from '../views/dc.vue'
import OCTG from '../views/octg.vue'
import Asset from '../views/asset.vue'
import OngoingOrders from '../views/Ongoingorders.vue'
import CompletedOrders from '../views/completedorders.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '*',
    redirect: '/login'
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    meta: {
      requiresAuth: true,
      displayname: 'Home'
    }
  },
  {
    path: '/racks',
    name: 'Racks',
    component: Racks
  },
  {
    path: '/test',
    name: 'Test',
    component: Test,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/navbar',
    name: 'navbar',
    component: Navbar,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/test',
    name: 'test',
    component: Test,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/inventory',
    name: 'inventory',
    component: Inventory,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/orderconfirm',
    name: 'orderconfirm',
    component: Orderconfirm,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/received',
    name: 'received',
    component: Received,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/preinvoice',
    name: 'preinvoice',
    component: Preinvoice,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/delivery',
    name: 'delivery',
    component: Delivery,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/dp',
    name: 'dp',
    component: DrillPipe,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/dc',
    name: 'dcollar',
    component: DrillCollar,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/hw',
    name: 'heavy',
    component: HeavyWeight,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/octg',
    name: 'octg',
    component: OCTG,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/asset',
    name: 'asset',
    component: Asset,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/ongoingorders',
    name: 'ongoingorders',
    component: OngoingOrders,
    meta: {
      requiresAuth: true,
      displayname: 'Ongoing Orders'
    }
  },
  {
    path: '/completedorders',
    name: 'completedorders',
    component: CompletedOrders,
    meta: {
      requiresAuth: true,
      displayname: 'Completed Orders'
    }
  },
  {
    path: '/racklocation',
    name: 'racklocation',
    component: Racklocation,
    meta: {
      requiresAuth: true,
      displayname: 'Rack Location'
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const currentUser = firebase.auth().currentUser
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  if (requiresAuth && !currentUser) next('login')
  else if (!requiresAuth && currentUser) next('Home')
  else next()
})

export default router
