import { createRouter, createWebHistory } from 'vue-router';
import UserLogined from '@/components/UserLogined.vue';
import MainDashboard from '@/components/MainDashboard.vue';
import AccessCreate from '@/components/AccessCreate.vue'; 
import AccessList from '@/components/AccessList.vue'; 
import AccessEdit from '@/components/AccessEdit.vue'; // Importar el nuevo componente

const routes = [
  {
    path: '/',
    name: 'UserLogined',
    component: UserLogined,

    meta: { requiresAuth: false }
  },
  {
    path: '/dashboard',
    name: 'MainDashboard',
    component: MainDashboard,
    meta: { requiresAuth: true },
    children: [
      {
        path: 'create',
        name: 'AccessCreate',
        component: AccessCreate
      },
      {
        path: 'list',
        name: 'AccessList',
        component: AccessList
      },
      {
        path: 'edit/:id',
        name: 'AccessEdit',
        component: AccessEdit
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('isAuthenticated');
  
  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
    next({ name: 'Login' });
  } else {
    next();
  }
});

export default router;
