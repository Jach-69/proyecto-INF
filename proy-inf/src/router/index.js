import { createRouter, createWebHistory } from 'vue-router';
import UserLogined from '@/components/UserLogined.vue';
import MainDashboard from '@/components/MainDashboard.vue';

const routes = [
  {
    path: '/',
    name: 'UserLogined',
    component: UserLogined,
  },
  {
    path: '/dashboard',
    name: 'MainDashboard',
    component: MainDashboard,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
