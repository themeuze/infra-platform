import React from 'react';

async function getExpertise() {
  // Hij pakt nu de URL uit de Azure settings, of valt terug op localhost voor lokaal testen
  const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';
  const res = await fetch(`${apiUrl}/api/expertise`, { cache: 'no-store' });
  
  if (!res.ok) throw new Error('Oeps! De backend is niet bereikbaar');
  return res.json();
}

export default async function Home() {
  const expertise = await getExpertise();

  return (
    <main className="min-h-screen bg-slate-50 p-8">
      <div className="max-w-4xl mx-auto">
        <header className="mb-12 border-b pb-6">
          <h1 className="text-4xl font-bold text-slate-900">NextGen Infra</h1>
          <p className="text-slate-600">Cloud & AI Expertise Platform op meuzeit.nl</p>
        </header>

        <section className="grid gap-6 md:grid-cols-3">
          {expertise.map((item: any) => (
            <div key={item.id} className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
              <h3 className="font-semibold text-lg text-blue-600">{item.title}</h3>
              <span className="inline-block mt-2 px-3 py-1 bg-blue-50 text-blue-700 text-xs rounded-full font-medium">
                {item.level}
              </span>
            </div>
          ))}
        </section>
      </div>
    </main>
  );
}