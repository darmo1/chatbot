"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export function Header() {
  const [isAuth, setIsAuth] = useState(false);
  const router = useRouter();
  const pathname = usePathname();

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (!token) {
      router.replace("/login");
    } else {
      setIsAuth(true);
    }
  }, []);

  useEffect(() => {
    if (isAuth && ["/", "/login", "/register"].includes(pathname)) {
      router.replace("/chat");
    }

    if (!isAuth && ["/", "/chat"].includes(pathname)) {
      router.replace("/login");
    }
  }, [isAuth, pathname, router]);

  return (
    <header className="bg-gray-800 text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        {isAuth ? (
          <button
            onClick={() => {
              localStorage.removeItem("access_token");
              setIsAuth(false)
              router.push("/login");
            }}
            className="text-white hover:underline mr-4"
          >
            Cerrar Sesión
          </button>
        ) : (
          <nav>
            <Link href="/login" className="text-white hover:underline mr-4">
              Login
            </Link>
            
          </nav>
        )}
      </div>
    </header>
  );
}
