import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 20 },
    { duration: '1m', target: 20 },
    { duration: '10s', target: 0 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

export default function () {
  const r = http.get('http://127.0.0.1:5001/productos/1/precio-final?descuento=10');
  check(r, { 'estado 200': (x) => x.status === 200 });
  sleep(1);
}